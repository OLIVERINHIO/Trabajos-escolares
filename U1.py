P={'Emilio','Guadalupe','David','Alexis','Vianey','Alexandra','Giovanny','Milka'}
J={'Paul','Luis','Isis','Milka','Ame','Martin','Astrid','Sarai','Alexa','Alexis'}

#a)¿Quines prefieren al menos un lenguaje?
union=P.union(J)
cruce= J.intersection(P)
R=union-cruce

print("Gente que prefiere un lenguaje:",R)

#b)¿Quienes prefieren ambos lenguajes?
#cruce= J.intersection(P)
print("Gente que prefirio Ambos Lenguajes:", cruce)

#c)¿Quienes prefieren solo Python?
C=P.difference(J)
print("Gente que prefirio PYTHON:", C)

#d)¿Quienes prefieren solo Java?
C2=J.difference(P)
print("Gente que prefirio JAVA:", C2)

#e)El numero total de alumnos que hicieron la encuesta
union=P.union(J)
print("El numero total de alumnos que hicieron la encuesta:", len(union))