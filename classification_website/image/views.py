from django.shortcuts import render
from .models_classification.all_models import Vgg16, ResNet50
from .forms import ResumeForm

# Создайте здесь представления.

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            image_path = f"media/files/{form.cleaned_data['image_file']}"
            form.save()
            list_names = ['first', 'second', 'third', 'forth', 'fifth']
            if form.cleaned_data['model'] == 'v16':
                vg16 = Vgg16()
                obj = vg16.image_classification(image_path)
                objects_percents = {}
                i = 0
                objects_percents["image"] = image_path.split('/')[-1]
                print(objects_percents["image"])
                for object_name, value in obj.items():
                    objects_percents[list_names[i]] = [object_name, str(round(float(value) * 100, 1))]
                    i += 1
                return render(request, 'file_classification_answer.html', objects_percents)
            elif form.cleaned_data['model'] == 'rn50':
                rs50 = ResNet50()
                obj = rs50.image_classification(image_path)
                objects_percents = {}
                i = 0
                objects_percents["image"] = image_path
                for object_name, value in obj.items():
                    objects_percents[list_names[i]] = [object_name, str(round(float(value) * 100, 1))]
                    i += 1
                return render(request, 'file_classification_answer.html', objects_percents)
    else:
        form = ResumeForm
    return render(request, 'file_upload.html', {'form': form})