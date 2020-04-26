from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from ranklist import models
import json
# Create your views here.

class MySerializers(serializers.ModelSerializer):
    """序列化"""
    class Meta:
        model = models.RankList
        fields = "__all__"


class Uploading_Score(APIView):
    """查询API"""
    def post(self,request):
        ret = {'status': True, 'error': None}
        ret = {'status':True}
        port_id = request.data.get('port')
        score = request.data.get('score')
        try:
            if not port_id:
                raise ValidationError('客户端号不能为空')
            print(isinstance(port_id,int))
            if not isinstance(port_id,int):
                if not port_id.isdecimal():
                    raise ValidationError('客户端号必须为整数')
            if not score:
                raise ValidationError('分数不能为空')
            if not isinstance(score,int):
                if not score.isdecimal():
                    raise ValidationError('分数必须为整数')
            client_object = models.RankList.objects.filter(port_id=port_id).first()
            if client_object:
                models.RankList.objects.filter(port_id=port_id).update(score=score)
            else:
                title = '客户端'+str(port_id)
                models.RankList.objects.create(port_id=port_id,title=title,score=score)
        except ValidationError as e:
            ret['status'] = False
            ret['error'] = str(e)
        return JsonResponse(ret)

class Select_Ranking(APIView):
    """获取排名API"""
    def get(self,request,port_id,begin,end):
        ret = {'status':True,'errormsg':None}
        try:
            if begin and end and int(begin) < int(end) and int(begin) < models.RankList.objects.count():
                rank_list_object = models.RankList.objects.values('port_id','title','score').order_by('-score')[int(begin)-1:int(end)]
            else:
                rank_list_object = models.RankList.objects.values('port_id','title','score').order_by('-score')
            if not rank_list_object:
                raise ValidationError('排行榜中没有数据')
            user_object = models.RankList.objects.values('port_id','title','score').filter(port_id=port_id).first()
            ser_all = MySerializers(instance=rank_list_object, many=True)
            ser_user = MySerializers(instance=user_object, many=False)
            ser_all_data = ser_all.data
            ser_user_data = ser_user.data
            index = 1
            for item in ser_all_data:
                item['index'] = index
                if ser_user_data['port_id'] == item['port_id']:
                    ser_user_data['index'] = index
                index += 1
                print(JsonResponse({'all':ser_all_data,'user':ser_user_data}))
                ret['all'] = ser_all_data
                ret['user'] = ser_user_data
        except Exception as e:
            ret['status'] = False
            ret['errormsg'] = str(e)
            return JsonResponse(ret)
        return JsonResponse(ret)
