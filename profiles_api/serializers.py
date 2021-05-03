from rest_framewok import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=155)