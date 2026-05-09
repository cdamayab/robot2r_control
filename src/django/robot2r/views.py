from django.shortcuts import render

def robot2r_view(request):
    return render(request, 'robot2r/robot2r_webgl.html')  # Renderiza la plantilla HTML

