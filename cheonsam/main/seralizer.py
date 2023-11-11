from rest_framework import serializers
from .models import *

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = "__all__"

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class Info_2_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Info_2
        fields = "__all__"

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ManualSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = "__all__"

class FactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facts
        fields = "__all__"


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"