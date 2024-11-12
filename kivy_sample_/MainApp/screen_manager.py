Screen_Manager = """
ScreenManager:
    MainScreen:
    HomeScreen:
    CountDownScreen:
    ToDoListScreen:     
    NotesScreen:
    StatisticsScreen:
    AchievementScreen:
    GamesScreen:
    AccountScreen:
    SettingsScreen:

<DrawerItem>
    active_indicator_color: "#e7e4c0"

    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        theme_icon_color: "Custom"
        icon_color: "#4a4939"

    MDNavigationDrawerItemText:
        text: root.text
        theme_text_color: "Custom"
        text_color: "#4a4939"

        
<DrawerLabel>
    adaptive_height: True
    padding: "18dp", 0, 0, "12dp"

    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        theme_icon_color: "Custom"
        icon_color: "#4a4939"
        pos_hint: {"center_y": .5}

    MDNavigationDrawerLabel:
        text: root.text
        theme_text_color: "Custom"
        text_color: "#4a4939"
        pos_hint: {"center_y": .5}
        padding: "6dp", 0, "16dp", 0
        theme_line_height: "Custom"
        line_height: 0


<MainScreen>:
    name: 'mainscreen'
    nav_layout: nav_layout
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDNavigationLayout:
            id: nav_layout  # Reference the MDNavigationLayout
            MDScreenManager:
                id: screen_manager
                
                HomeScreen:
                    name: 'homescreen'
                    MDScreen:  # Add an MDScreen here
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Welcome to Home Screen"
                        halign: "center"
                CountDownScreen:
                    name: 'countdownscreen'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Countdown Screen"
                        halign: "center"
                ToDoListScreen:   
                    name: 'todolist'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "To-Do List Screen"
                        halign: "center"  
                NotesScreen:
                    name: 'notes'
                    MDScreen:  # Add an MDScreen here 
                        MDLabel:
                            text: "Note"
                            pos_hint: {"center_y": .95}
                            theme_text_color: "Custom"
                            text_color: "black"
                            font_name: "Montaser Arabic"
                            font_size: "24sp"
                            bold: True
                            size_hint_x: .42
                            halign: "left"
                            pos_hint: {"center_x": .55, "center_y": .75}
                        


                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"

                StatisticsScreen:
                    name: 'statistics'
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Statistics Screen"
                        halign: "center"
                    Button:
                        text: "Go to Achievement"
                        font_name: "Tahoma"
                        size_hint: .8, .09 
                        font_size: "18sp"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        background_color: 0,0,0,0
                        on_release: app.go_to_achievement()
                        canvas.before:
                            Color:
                                rgb: app.btn_color
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [8]



                GamesScreen:
                    name: 'games'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Games Screen"
                        halign: "center"
                AccountScreen:
                    name: 'account'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Account Screen"
                        halign: "center"
                SettingsScreen:
                    name: 'settings'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Settings Screen"
                        halign: "center"
                                
            MDNavigationDrawer:
                id: nav_drawer
                radius: 0, dp(16), dp(16), 0

                MDNavigationDrawerMenu:

                    MDNavigationDrawerHeader:
                        orientation: "vertical"
                        padding: 0, 0, 0, "12dp"
                        adaptive_height: True

                        MDLabel:
                            text: "Title"
                            theme_text_color: "Custom"
                            theme_line_height: "Custom"
                            line_height: 0
                            text_color: "#4a4939"
                            adaptive_height: True
                            padding_x: "16dp"
                            font_style: "Display"
                            role: "small"

                        MDLabel:
                            text: "...."
                            padding_x: "18dp"
                            adaptive_height: True
                            font_style: "Title"
                            role: "large"

                    MDNavigationDrawerDivider:

                    DrawerItem:
                        icon: "home"
                        text: "Home"
                        on_release: screen_manager.current = 'homescreen'

                    DrawerItem:
                        icon: "clock-outline"
                        text: "Count down"
                        on_release: screen_manager.current = 'countdownscreen'
                    
                    DrawerItem:
                        icon: "clipboard-list"
                        text: "To-do-list"
                        on_release: screen_manager.current = 'todolist'
                    
                    DrawerItem:
                        icon: "note-edit-outline"
                        text: "Note"
                        on_release: screen_manager.current = 'notes'

                    DrawerItem:
                        icon: "chart-bar"
                        text: "Statistics"
                        on_release: screen_manager.current = 'statistics'
                        
                    DrawerItem:
                        icon: "gamepad-variant"
                        text: "Game"
                        on_release: screen_manager.current = 'games'
                        
                    DrawerItem:
                        icon: "account"
                        text: "Profile"
                        on_release: screen_manager.current = 'account'
                
                    MDNavigationDrawerDivider:
                        size_hint_y: None
                        height: "1dp"
                                            
                    DrawerItem:
                        icon: "cog"
                        text: "Settings"
                        on_release: screen_manager.current = 'settings'
                        
                    DrawerItem:
                        icon: "logout"
                        text: "Log out"
                        on_release: root.manager.current = 'login'

"""
