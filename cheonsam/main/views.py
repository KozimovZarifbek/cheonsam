from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from main.seralizer  import *


@api_view(['GET'])
def get_banner(request):
       banner = Banner.objects.all()
       serialized_data = BannerSerializer()
       return Response(serialized_data.data)

@api_view(['POST'])
def order_view(request):
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       order = Order.objects.create(
              name=name,
              phone=phone,
       )
       ser = OrderSerializer(order).data
       return Response(ser)

@api_view(['GET'])
def get_species(request):
       species = Species.objects.all()
       serialized_data =SpeciesSerializer(species,many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_info(request):
       info = Info.objects.all()
       serialized_data = InfoSerializers(info,many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_info_2(request):
       info = Info_2.objects.all()
       serialized_data = Info_2_Serializers(info,many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_company(request):
       company = Company.objects.all()
       serialized_data = CompanySerializers(company,many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_question(request):
       question = Question.objects.all()
       serialized_data = QuestionSerializers(question,many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_manual(request):
       manual = Manual.objects.all()
       serialized_data = ManualSerializers(manual,many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_facts(request):
       facts = Facts.objects.all()
       serialized_data = FactsSerializers(facts,many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_feedback(request):
       feedback = Feedback.objects.all()
       serialized_data = FeedbackSerializers(feedback,many=True).data
       return Response(serialized_data)



