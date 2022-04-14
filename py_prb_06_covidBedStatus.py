runtime = 5
list = ['101', 'Delhi', 'Delhi', '100000', '20000', '5000', '2000', 
'102', 'Telangana', 'Hyderabad', '200000', '40000', '1000', '500',
'103', 'Telangana', 'Warangal', '100000', '30000', '2000', '1000',
'104', 'AndhraPradesh', 'Vijayawada', '800000', '300000', '30000', '2500',
'105', 'AndhraPradesh','Vizag','500000','100000','6000','1000','AndhraPradesh']
# ,'Vizag','500000','100000','6000','1000','AndhraPradesh'
getcityocubeds = list[-1]
c_map = {}
commonstate = {}
def collectcityinfo():
    count = 0
    jump=7  
    fi_cycode=0
    fi_cystate=1
    fi_cyname=2
    fi_cycovb=3
    fi_cycoav=4
    fi_cyven=5
    fi_cyavaven=6     
    for i in range(runtime):
        if count ==0:
            count+=1
            City(state_name=list[fi_cystate],city_name=list[fi_cyname],
                 covidbeds=int(list[fi_cycovb]),
                avlblcovbeds=int(list[fi_cycoav]),
                ventilbeds=int(list[fi_cyven]),
                avlblventilbeds=int(list[fi_cyavaven])) 
        else:
            j=jump*i
            City(state_name=list[fi_cystate+j],city_name=list[fi_cyname+j],
                 covidbeds=int(list[fi_cycovb+j]),
                avlblcovbeds=int(list[fi_cycoav+j]),
                ventilbeds=int(list[fi_cyven+j]),
                avlblventilbeds=int(list[fi_cyavaven+j]))
    _sorted = sorted(c_map)
    for i in _sorted:
        print(f'{i} {c_map[i][0]} {c_map[i][1]}')
    if getcityocubeds not in commonstate:
        print('No city available')
    else:
        for i in commonstate[getcityocubeds]:
            print(f'{i}',end=" ") 
class City():
      def __new__(self,city_id=0,state_name='NA',city_name='NA',covidbeds=0,avlblcovbeds=0,ventilbeds=0,avlblventilbeds=0):
        self.city_id = city_id #101
        self.state_name = state_name #Delhi
        self.city_name = city_name #Delhi
        self.covidbeds=covidbeds #100000
        self.avlblcovbeds=avlblcovbeds #20000      #Delhi 20000 2000
        self.ventilbeds =ventilbeds #5000
        self.avlblventilbeds=avlblventilbeds #2000
        if getcityocubeds in commonstate:
            a=commonstate[state_name]
            if a[1]<(covidbeds-avlblcovbeds):
                commonstate[state_name]=[city_name,covidbeds-avlblcovbeds,ventilbeds-avlblventilbeds]
        else:
            commonstate[state_name]=[city_name,covidbeds-avlblcovbeds,ventilbeds-avlblventilbeds]            
        if state_name in c_map:
            a=c_map[state_name]
            c_map[state_name]=[a[0]+avlblcovbeds,a[1]+avlblventilbeds]
        else:
            c_map[state_name] = [avlblcovbeds,avlblventilbeds]                    
# get info
collectcityinfo()  
       