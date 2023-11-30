#!/usr/bin/env python
# coding: utf-8

# In[16]:


class nuclide:
    def __init__(self, Z, A):
        self.A = A
        self.Z = Z

    def neutron_number_cal(self):
        return self.A - self.Z

proton_number = int(input('please enter proton number of your nuclide'))
atomic_number = int(input('please enter atomic number of your nuclide'))
if atomic_number>=proton_number:
    your_nuclide = nuclide(proton_number, atomic_number)
    neutron_number = your_nuclide.neutron_number_cal()
    print('neutron number is:', neutron_number)
else: print('ERROR: atomic number should be larger than or  equal to the proton number')


# In[ ]:




