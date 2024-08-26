from flask_admin import Admin
from flask_wtf.file import FileField
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import secure_filename
from flask_login import current_user
from models import db, Profile, Specialization, EducationalExperience, Pricing, FeaturedProject, Advantage, User
import boto3, os
from botocore.exceptions import NoCredentialsError



BUCKET_NAME = 'portfolio_bucket'


s3_client = boto3.client(
    's3',
    region_name=os.getenv('REGION'),
    endpoint_url=os.getenv('ENDPOINT'),
    aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('ACCESS_KEY'),
    config=boto3.session.Config(signature_version='s3v4')
)

def generate_presigned_url(file_key,  expiration=315360000):
    try:
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': file_key},
            ExpiresIn=expiration
        )
        return presigned_url
    except Exception as e:
        print(f"Error generating presigned URL: {e}")
        return None

class CustomFileUploadField(FileField):
    def __init__(self, label='', **kwargs):
        super().__init__(label, **kwargs)
    
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0]

    def save(self, filename):
        if self.data:
            file_key = secure_filename(filename)
            try:
                s3_client.upload_fileobj(self.data, BUCKET_NAME, file_key)
                file_url = generate_presigned_url(file_key)
                return file_url
            
                print('URL returned successfully' + file_url)
            except NoCredentialsError:
                print("Credentials not available.")
            except Exception as e:
                print(f"Error uploading file: {e}")
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
