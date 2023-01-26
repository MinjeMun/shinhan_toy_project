from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Member

class MemberSerializer(serializers.ModelSerializer):

    # 유효성 검사
    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('비밀번호는 6자 이상 필요합니다.')
        return make_password(value)

    class Meta:
        model = Member
        fields = ('id','username','password','tel',)
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'password': { 
                'write_only': True, 
            },
        }