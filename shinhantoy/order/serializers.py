from rest_framework import serializers
from .models import Order, Comment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    # 로그인 된 정보(CurrentuserDefault)를 자동으로 불러옴
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required=False
    )

    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )
    member_username = serializers.SerializerMethodField()
    # MethodField() - 데이터를 가져갈 때 정의 가능한 custom field
    # get_변수명(MethodField) 로 함수를 정의해줘야 갖고 옴 -> 둘은 무조건 같이 작성됨
    
    def get_member_username(self, obj):
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'