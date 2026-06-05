import re

filepath = r'c:\Users\manda\OneDrive\Documents\Clinic_TrackPro\templates\settings.html'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update the clinic profile form inputs
old_inputs = '''                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-2">Clinic Name</label>
                    <input type="text" name="clinic_name" value="{{ settings.clinic_name if settings else 'ClinicTrack Pro' }}" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-colors" required>
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-2">Logo URL (Optional)</label>
                    <input type="url" name="logo_url" value="{{ settings.logo_url if settings else '' }}" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-colors" placeholder="https://...">
                </div>'''

new_inputs = '''                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-2">Clinic Name</label>
                    <input type="text" name="clinic_name" value="{{ settings.clinic_name if settings else 'ClinicTrack Pro' }}" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-colors" required>
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-2">Primary Doctor Name</label>
                    <input type="text" name="doctor_name" value="{{ settings.doctor_name if settings else '' }}" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-colors" placeholder="Dr. John Doe">
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-2">Phone Number</label>
                    <input type="text" name="phone" value="{{ settings.phone if settings else '' }}" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-colors" placeholder="+1 234 567 8900">
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-2">Logo URL (Optional)</label>
                    <input type="url" name="logo_url" value="{{ settings.logo_url if settings else '' }}" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-colors" placeholder="https://...">
                </div>'''

c = c.replace(old_inputs, new_inputs)

# 2. Add onclick to Add Doctor button
old_btn = '''<button class="inline-flex items-center justify-center gap-2 bg-white border border-slate-200 text-slate-700 px-4 py-2 rounded-xl text-sm font-medium hover:bg-slate-50 transition-colors shadow-sm">
                <i data-feather="user-plus" class="w-4 h-4"></i> Add Doctor
            </button>'''

new_btn = '''<button onclick="document.getElementById('addDoctorModal').classList.remove('hidden')" type="button" class="inline-flex items-center justify-center gap-2 bg-white border border-slate-200 text-slate-700 px-4 py-2 rounded-xl text-sm font-medium hover:bg-slate-50 transition-colors shadow-sm">
                <i data-feather="user-plus" class="w-4 h-4"></i> Add Doctor
            </button>'''

c = c.replace(old_btn, new_btn)

# 3. Fix delete doctor button
old_del = '''<button class="text-slate-400 hover:text-red-600 p-2 rounded-lg hover:bg-red-50 transition-colors" title="Remove">
                            <i data-feather="trash-2" class="w-4 h-4"></i>
                        </button>'''
new_del = '''<form action="/settings/doctors/{{ doc.id }}/delete" method="post" class="inline">
                            <button type="submit" class="text-slate-400 hover:text-red-600 p-2 rounded-lg hover:bg-red-50 transition-colors" title="Remove" onclick="return confirm('Are you sure you want to remove this doctor?');">
                                <i data-feather="trash-2" class="w-4 h-4"></i>
                            </button>
                        </form>'''
c = c.replace(old_del, new_del)

# 4. Add the modal at the bottom before {% endblock %}
modal_html = '''
<!-- Add Doctor Modal -->
<div id="addDoctorModal" class="hidden fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-50 flex justify-center items-center">
    <div class="bg-white rounded-2xl w-full max-w-md shadow-2xl p-6 mx-4">
        <div class="flex items-center justify-between mb-6">
            <h3 class="text-lg font-bold text-slate-800">Add New Doctor</h3>
            <button type="button" onclick="document.getElementById('addDoctorModal').classList.add('hidden')" class="text-slate-400 hover:text-slate-600">
                <i data-feather="x" class="w-5 h-5"></i>
            </button>
        </div>
        <form action="/settings/doctors/new" method="post" class="space-y-4">
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Name</label>
                <input type="text" name="name" class="w-full px-4 py-2 border border-slate-200 rounded-xl text-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20" required>
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Degree</label>
                <input type="text" name="degree" placeholder="e.g., MD, MBBS" class="w-full px-4 py-2 border border-slate-200 rounded-xl text-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Specialization</label>
                <input type="text" name="specialization" placeholder="e.g., Cardiology" class="w-full px-4 py-2 border border-slate-200 rounded-xl text-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Phone</label>
                <input type="text" name="phone" class="w-full px-4 py-2 border border-slate-200 rounded-xl text-sm focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20">
            </div>
            <div class="pt-4 flex justify-end gap-3">
                <button type="button" onclick="document.getElementById('addDoctorModal').classList.add('hidden')" class="px-5 py-2 rounded-xl text-slate-600 bg-slate-100 hover:bg-slate-200 font-medium transition-colors">Cancel</button>
                <button type="submit" class="px-5 py-2 rounded-xl text-white bg-blue-600 hover:bg-blue-700 font-medium transition-colors shadow-sm">Save Doctor</button>
            </div>
        </form>
    </div>
</div>
'''

if 'id="addDoctorModal"' not in c:
    c = c.replace('{% endblock %}', modal_html + '\n{% endblock %}')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated settings.html')
