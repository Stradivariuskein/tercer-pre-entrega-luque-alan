++++++++++++++++++++++++++**IMPORTANTE**+++++++++++++++++++++++++++++++++

Intale los requerimientos : pip install -r requirements.txt 
usuario: ad@admin.com contraseña: 369258147pepe 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Turno para psicologia video explicativo: https://www.youtube.com/watch?v=YiBQzcy9BcE 
Pagina autogestion de turnos para sesion con psicologa. hay sierta rutas bloquedas para los usuario q no son administradores /administration/*

Tiene 5 apps: home: carta de presentacion de la psicologa views: home: muestra foto de portada y distintas secciones editables para el administrador. curriculum: muestra un poco de informacion sobre mi.

    urls:
        home/
        curriculum/

login: se encarga de registrar y autenticar ususarios
    models: 
        Acount: este modelo esta vinculado al modelo User de django y agrega datos extra como fecha de nacimiento y telefono.

    views: 
        Register: registra un nuevo usuario en la tabla auth_user.
        user_logout: desloguea un usuario.
        register_acount: crea una cuenta vinculada al usuario actualemnte loguiado.
        view_login: la vista del login para incicar sesion
    
    urls:
       login/
       register/
       register/acount/
       logout/



agenda: se encarga de la edicion de tu perfil, reservar y mostrar turnos disponibles.
    models:
        TypeSession: tipo de sesion (presencial o remoto, en grupo o solo, tiene obra social(true/false)) esta vinculado a los turnos
        Turn: el turno tiene fecha hora de inicio, hora de finalizacion y tipo de sesion

    views: 
        get_turn: cartel de confirmacion de la reservar del turno.
        turnCreate: crea y almacena el turno en la base de datos.
        turnos_disponibles: genera una listasta con los trunos disponibles. si el usuario actual es administrado es redirigido a admin-turn
        perfil: modifica el perfil de ususario actualmente autenticado.
        my_turns: muestra todos los turnos corespondientes al usuario actual y los puede cancelar

    
    urls:
        getTurn/
        turnCreate/
        turnos/
        perfil/
        typeSession/
        cuentas/

administration: se encarga de gestionar lo q muestra home;
                editar y borrar cuentas;
                crear, editar y borrar turnos;
                crear, editar y borrar tipos de session.
                -> solo accesible para el usario administrador <-
    models:
        homeSection: secciones q pareceran el home.
        HomeFields: lo q muestra la portada de home.

    views:
        TypeSessionCreate: crea un tipo de sesion
        TypeSessionUpdate: modifica un tipo de sesion
        TypeSessionDelete: elimina un tipo de sesion
        AcountListView: muestra todas la cuentas de las vaces de datos
        AccountDelet: elimina una cuenta
        AccountUpdate: modifica una cuenta
        HomeUpdate: actualiza los campos de la portada de home
        HomeSectionCreate: crea una nueva seccion para home
        HomeSectionUpdate: modifica uns seccion para home
        HomeSectionDelete: elimina una seccion para home
        home_edit: muestra los campos de home y todas las secciones
        TurnUpdate: modifica un turno
        turnCreate: el administrado puede crear un nuevo turno para un usuario espesifico
        admin_turn: muestra todos los turno agendados por semanas
    urls:
        typeSession/
        typeSession/create/
        typeSession/update/<int:pk>/
        typeSession/delete/<int:pk>/

        cuentas/
        cuentas/update/<int:pk>/
        cuentas/delete/<int:pk>/

        home/edit
        home/update/<int:pk>/
        home/section/create/
        home/section/update/<int:pk>/
        home/section/delete/<int:pk>/

        turns/<int:p_week>/
        edit-turn/<int:pk>/
        turns/create/

core: alacena las platillas comunes para toda la pagina no tiene nada mas.
    templates:
        navBar.html
        base.html
