Screen_Manager = """
ScreenManager:
    MainScreen:
    HomeScreen:
    CountDownScreen:
    ToDoListScreen:     
    NotesScreen:
    StatisticsScreen:
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
                        text: "Notes Screen"
                        halign: "center"
                StatisticsScreen:
                    name: 'statistics'
                    MDScreen:  # Add an MDScreen here
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: 20
                            spacing: 20
                            md_bg_color: [248/255, 245/255, 251/255, 1]

                            MDLabel:
                                text: "STATISTICS"
                                halign: "center"
                                font_style: "H5"
                                theme_text_color: "Custom"
                                text_color: [0.1, 0.1, 0.2, 1]

                            MDBoxLayout:
                                orientation: 'horizontal'
                                spacing: 20

                                MDCard:
                                    orientation: "vertical"
                                    padding: 15
                                    radius: [25, 25, 25, 25]
                                    md_bg_color: [1, 1, 1, 1]
            
                                    MDLabel:
                                        text: "🔥"
                                        halign: "center"
                                        font_style: "H2"
                                        
                                    MDLabel:
                                        id: current_streak
                                        text: "0"
                                        halign: "center"
                                        font_style: "H3"
                                        
                                    MDLabel:
                                        text: "Current Streak"
                                        halign: "center"
                                        
                                        
                                    MDLabel:
                                        id: max_streak
                                        text: "Highest Streak: 0"
                                        halign: "center"
                                        
                                        
                                    MDLabel:
                                        text: "On average of: 1h45m per opening"
                                        halign: "center"
                                        
                                        
                                    MDLabel:
                                        id: completion_probability
                                        text: "Probability of: 0% completing a cycle"
                                        halign: "center"
                                        

                                MDCard:
                                    orientation: "vertical"
                                    padding: 15
                                    radius: [25, 25, 25, 25]
                                    md_bg_color: [1, 1, 1, 1]
                                    size_hint_x: None
                                    width: "200dp"

                                    MDLabel:
                                        id: completion_percentage
                                        text: "0%"
                                        halign: "center"
                                        font_style: "H4"
                                        
                                    MDLinearProgressIndicator:
                                        id: completion_bar
                                        value: 0
                                        color: [0, 0, 0, 1]
                                        size_hint_y: None
                                        height: "10dp"
                                        
                                    MDLabel:
                                        text: "Completed"
                                        halign: "center"
                                        
                                        
                                    MDLabel:
                                        text: "Fail"
                                        halign: "center"
                                        

                            MDLabel:
                                text: "Achievements"
                                halign: "center"
                                
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