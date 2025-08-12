from flask_admin import Admin
from flask_wtf.file import FileField
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import secure_filename
from flask_login import current_user
from models import db, Profile, Specialization, EducationalExperience, Pricing, FeaturedProject, Advantage, User
import os
from flask import current_app

class CustomFileUploadField(FileField):
    def __init__(self, label='', **kwargs):
        super().__init__(label, **kwargs)
    
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0]

    def save(self, filename):
        if self.data:
            # Secure the filename and create unique name
            filename = secure_filename(filename)
            # Add timestamp to make filename unique
            import time
            timestamp = str(int(time.time()))
            name, ext = os.path.splitext(filename)
            unique_filename = f"{name}_{timestamp}{ext}"
            
            # Ensure upload directory exists
            upload_folder = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)
            
            # Save file to local storage
            file_path = os.path.join(upload_folder, unique_filename)
            self.data.save(file_path)
            
            # Return the relative URL for the file
            return f"/static/uploads/{unique_filename}"
        return None

class CustomImageAdminView(ModelView):
    
    def is_accessible(self):
        return current_user.is_authenticated

    form_overrides = {
        'image_url': CustomFileUploadField
    }

    def on_model_change(self, form, model, is_created):
        if form.image_url.data:
            filename = form.image_url.data.filename
            file_url = form.image_url.save(filename)
            model.image_url = file_url
        return super(CustomImageAdminView, self).on_model_change(form, model, is_created)

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

def setup_admin(app):
    admin = Admin(app, name='NOOB ADMIN', template_mode='bootstrap3')
    admin.add_view(AdminView(User, db.session))
    admin.add_view(CustomImageAdminView(Profile, db.session))
    admin.add_view(AdminView(Pricing, db.session))
    admin.add_view(CustomImageAdminView(FeaturedProject, db.session))
    admin.add_view(AdminView(EducationalExperience, db.session))
    admin.add_view(AdminView(Specialization, db.session))
    admin.add_view(CustomImageAdminView(Advantage, db.session))
