print('--------------Expert System------------------')

print('Answer the following question in yes or no.')

F=str(input('Do you have fever? \t: ')).lower().strip()
C=str(input('Do you have cough? \t: ')).lower().strip()
HA=str(input('Do you have headache? \t: ')).lower().strip()

print('============Disgnosis=====================')

if(F=='no' and C=='no' and HA=='no'):
    print('You seem to be healthy.')
    
elif(F=='yes' and C=='no' and HA=='no'):
    print('You may have a Mild Infection.')
    
elif(F=='no' and C==yes and HA=='no'):
    print('You may have a Throat Infection or Mild cold.')
    
elif(F=='no' and C=='no' and HA=='yes'):
     print('You may have a Stress, Migratine or Fatigue.')
     
elif(F=='no' and C=='no' and HA=='yes'):
     print('You may have a Stress, Migratine or Fatigue.')
     
elif(F=='yes' and C=='yes' and HA=='no'):
     print('You may have Flu.')

elif(F=='yes' and C=='no' and HA=='yes'):
     print('You may have Viral Infection.')

elif(F=='no' and C=='yes' and HA=='yes'):
     print('You may have Comman Cold.')

elif(F=='yes' and C=='yes' and HA=='yes'):
     print('You may have Flu or a Viral Infection.')

