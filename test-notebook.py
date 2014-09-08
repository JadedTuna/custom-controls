import ui
import notebook
reload(notebook)

view = ui.View()

notebook = notebook.Notebook()
notebook.width = 300
notebook.height = 300
view1 = ui.View()
view1.bg_color = "blue"
button = ui.Button(title="Button1")

view1.add_subview(button)

view2 = ui.View()
view2.bg_color = "red"
label = ui.Label()
label.width = 300
label.text = "Custom Controls"
view2.add_subview(label)

table = ui.TableView()
table.data_source = ui.ListDataSource(["item1", "item2"])
table.flex = "WH"

notebook.addPage("Blue", view1)
notebook.addPage("Red",  view2)
notebook.addPage("TableView here", table)
view.add_subview(notebook)
view.present("sheet")
