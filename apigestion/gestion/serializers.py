from rest_framework.serializers import ModelSerializer

from models import Article

class ArticleListSerializer(ModelSerializer):
    models = Article
    fields='__all__'

def validate_price(self,value ):

    if value<1:
        raise serializers.ValidationError('le prix ne peut etre inferieur a 1 dollar')
    return value 

def validate_price(self,value ):

    if value<1:
        raise serializers.ValidationError('le prix ne peut etre inferieur a 1 dollar')  
    return value

def validate_name(self,data):
    if Article.objects.filter(name=data).exists():
        raise serializers.ValidationError('le nom existe deja')


class ArticleDetailSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Article
        fields =['id','name','quantite','price','description']

