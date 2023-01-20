from rest_framework import serializers
from .models import Images, Persons, PersonAndImages


class ImageSerializer(serializers.Serializer):
    photo = serializers.ImageField()
    geolocation = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    persons_names = serializers.CharField()

    def create(self, validated_data):
        persons_names = validated_data['persons_names']
        if ',' in persons_names:
            split_person = persons_names.split(',')
        else:
            split_person = persons_names.split()
        get_image = None
        image_pk = None
        for person in split_person:
            if person not in Persons.objects.all():
                person = person.strip()
                get_person, create = Persons.objects.get_or_create(name=person)
                if create:
                    get_person.save()
                if image_pk:
                    get_image = Images.objects.get(pk=image_pk)
                else:
                    get_image = Images.objects.create(photo=validated_data['photo'],
                                                      description=validated_data['description'],
                                                      geolocation=validated_data['geolocation'])
                image_pk = get_image.pk
                if image_pk:
                    PersonAndImages.objects.create(photo_pk=get_image, person_pk=get_person)
                get_image.save()

        return get_image


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('name',)


class ImageSerializerList(serializers.Serializer):
    photo = serializers.ImageField()
    geolocation = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    persons_names = PersonSerializer(read_only=True, many=True)


class PersonSearchSerializer(serializers.ModelSerializer):
    name = ImageSerializerList(read_only=True, many=True)

    class Meta:
        model = Persons
        fields = ['name']