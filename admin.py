from flask_admin.form import BaseForm
from flask_admin import Admin
from flask_wtf.file import FileField
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import secure_filename
import os
from flask_login import current_user
from models import db, Profile, Specialization, EducationalExperience, Pricing, FeaturedProject, Advantage, User



UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class CustomFileUploadField(FileField):
    def __init__(self, label='', **kwargs):
        super().__init__(label, **kwargs)

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0]

    def save(self, filename, folder):
        if self.data:
            filepath = os.path.join(folder, secure_filename(self.data.filename))
            self.data.save(filepath)
            return os.path.join('uploads', filename)
        return None

class CustomImageAdminView(ModelView):
    
    def is_accessible(self):
        return current_user.is_authenticated

    form_overrides = {
        'image_url': CustomFileUploadField
    }

    def on_model_change(self, form, model, is_created):
        if form.image_url.data:
            filename = secure_filename(form.image_url.data.filename)
            folder = UPLOAD_FOLDER
            filepath = form.image_url.save(filename, folder)
            model.image_url = filepath
        return super(CustomImageAdminView, self).on_model_change(form, model, is_created)
    
class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated




# Initialize Flask-Admin and add views
def setup_admin(app):
    admin = Admin(app, name='NOOB ADMIN', template_mode='bootstrap3')
    admin.add_view(AdminView(User, db.session))
    admin.add_view(CustomImageAdminView(Profile, db.session))
    admin.add_view(AdminView(Pricing, db.session))
    admin.add_view(CustomImageAdminView(FeaturedProject, db.session))
    admin.add_view(AdminView(EducationalExperience, db.session))
    admin.add_view(AdminView(Specialization, db.session))
    admin.add_view(CustomImageAdminView(Advantage, db.session))
