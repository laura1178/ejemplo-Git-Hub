from kivy.app import App
class TaskManagerApp (App):
    def build (self):
        self.load_data()
        self.layout = BoxLayout(orientation='vertical')
#agregr tarea 
self.add_task_layout = BoxLayout(size_hint_y=None, height=40)
self.task_input = TextInput(hint_text='escribe una nueva tarea')
self.add_button = Button(ttext='agregar',size_hint_x=None, width=100)
self.add_button.bind(on_press=self.add_task)
self.add_task_layout.add_widget(self.task_input)
self.add_task_layout.add_widget(self.add_button)
self.layout.add_widget(self.add_task_layout)
#lista de tareas
self.add_task_layout = BoxLayout(orientation='vertical')
self.layout.add_widget(self.task_list_layout)
self.update_task_list()