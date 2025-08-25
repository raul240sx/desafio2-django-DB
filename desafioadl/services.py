from .models import Tarea, SubTarea


## FUNCIONA PARA IMPRIMIR TODAS LAS TAREAS Y SUBTAREAS ##
def imprimir_en_pantalla():
    tareas = Tarea.objects.all()
    for t in tareas:
        print(f"Tarea {t.id}: descripción: {t.descripcion}, tarea eliminada: {t.eliminada}")
        if hasattr(t, "subtarea"):
            for s in t.subtarea.all().order_by("id"):
                print(f"  └─ Subtarea {s.id}: {s.descripcion}, eliminada: {s.eliminada}")


## FUNCION PARA CREAR UNA NUEVA TAREA ##
def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    imprimir_en_pantalla()


## FUNCION PARA TERMINAR UNA TAREA ## 
def borrar_tarea(id):
    tarea = Tarea.objects.get(id=id)
    tarea.eliminada = True
    tarea.save()
    imprimir_en_pantalla()


## FUNCION PARA CREAR UNA SUBTAREA ##
def crear_sub_tarea(tarea, descripcion_subtarea):
    tarea = Tarea.objects.get(id=tarea)
    sub_tarea = SubTarea(tarea_id=tarea, descripcion=descripcion_subtarea)

    sub_tarea.save()
    imprimir_en_pantalla()


##  FUNCION PARA TERMINAR UNA SUBTAREA ##
def borrar_sub_tarea(subtarea_id):
    sub_tarea = SubTarea.objects.get(id=subtarea_id)
    sub_tarea.eliminada = True
    sub_tarea.save()
    imprimir_en_pantalla()


## FUNCION PARA RECUPERAR TAREA Y SUBTAREAS ##
def recuperar_tarea_y_subtareas(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = False
    tarea.save()
    if hasattr(tarea, "subtarea"):
        tarea.subtarea.filter(eliminada=True).update(eliminada=False)
    imprimir_en_pantalla()


## FUNCION PARA RECUPERAR UNA SUBTAREA ##
def recuperar_subtarea(id_subtarea):
    subtarea = SubTarea.objects.get(id=id_subtarea)
    subtarea.eliminada = False
    subtarea.save()
    imprimir_en_pantalla()


## FUNCION PARA ELIMINAR UNA TAREA DE LA DB ##
def eliminar_tarea(id_tarea):
    Tarea.objects.get(id=id_tarea).delete()
    imprimir_en_pantalla()


## FUNCION PARA ELIMINAR UNA SUBTAREA DE LA DB ##
def eliminar_subtarea(id_subtarea):
    SubTarea.objects.get(id=id_subtarea).delete()
    imprimir_en_pantalla()