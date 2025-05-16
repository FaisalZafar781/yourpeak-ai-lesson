from django.contrib.auth.models import User
from lesson_plans.models import UserProfile

# For user 'admin'
user = User.objects.get(username='admin')
UserProfile.objects.get_or_create(user=user, defaults={'role': 'admin'})

# For user 'snake'
user = User.objects.get(username='snake')
UserProfile.objects.get_or_create(user=user, defaults={'role': 'client'})

# For user 'user'
user = User.objects.get(username='user')
UserProfile.objects.get_or_create(user=user, defaults={'role': 'client'})

# from pinecone import Pinecone, ServerlessSpec


# pc = Pinecone(api_key="")

# index_name = "lesson-index"

# pc.create_index(
#         name=index_name, 
#         dimension=3072,
#         metric='cosine',
#         spec=ServerlessSpec(cloud='aws', region='us-east-1')
#     )