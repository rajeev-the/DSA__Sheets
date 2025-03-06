data =[
     ["S.No", "Question", "Link", "Company"],
    [1, "Equilibrium Point " , " https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?page=1&category=Arrays&sortBy=submissions" , " Amazon,Adobe,Google,Facebook,Microsoft,Uber, " ]
]

with open("C:\DSA_sheet\DSA\Arrays\Prefix_sum\Questions.txt","w") as file:
    for row in data:
      file.write("{:<5} {:<10} {:<5} {:<15}\n".format(*row))