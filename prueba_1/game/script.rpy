label start:
    scene vilmaRopa with dissolve  
    vilma"¿Hola que parte de mi ropa te gusta?" 

    $eleccion=renpy.imagemap("vilmaRopa","vilmaSinRopa",
    [
        (380,480,980,600,"falda"),
        (500,250,980,400,"pecho")

    ])

    if eleccion=="falda":
        vilma"Te gusta lo que hay debajo de la falda"
    else:
        vilma"Te gusta mis tetas redonditas"
         
        
   

   