from django.shortcuts import render

# Create your views here.
def compatibility_checker(request):
    chemicals = Chemical.objects.all()

    result = None
    if request.method == 'POST':
        chem1_id = request.POST.get('chemical1')
        chem2_id = request.POST.get('chemical2')
        chem1 = Chemical.objects.get(id=chem1_id)
        chem2 = Chemical.objects.get(id=chem2_id)

        # Simple example logic (you can expand later)
        if chem1.hazard_rating == 'High' and chem2.hazard_rating == 'High':
            result = f"{chem1.name} and {chem2.name} might react dangerously! ⚠️"
        else:
            result = f"{chem1.name} and {chem2.name} seem compatible. ✅"

    return render(request, 'tannerychem/compatibility_checker.html', {
        'chemicals': chemicals,
        'result': result
    })
