import ui
from collections import OrderedDict

class Notebook(ui.View):
    def __init__(self):
        ui.View.__init__(self)
        self.pages    = OrderedDict()
        self.selpage  = None
        self.tappage  = None
        self.touchid  = None
        self.tabpad   = 10
        self.tabfg    = 0.1
        self.tabfont  = ("Courier", 14)
        self.bg_color = 0.75
    
    def addPage(self, page, view):
        self.pages[page] = view
        self.selpage = view
        #view.x += self.x
        #view.y += self.y
        view.frame = (view.x + self.x,
                      view.y + self.y,
                      self.width,
                      self.height)
        for _view in self.pages.values():
            if _view != view:
                _view.hidden = True
        self.add_subview(view)
    
    def setPage(self, page):
        view = self.pages[page][0]
        view.hidden = False
        for [_view, _, _] in self.pages.values():
            if _view != view:
                _view.hidden = True
    
    def draw(self):
        x = y = 0
        radius = 5
        for page, view in self.pages.items():
            w, h = [i for i in ui.measure_string(page, 0, self.tabfont)]
            dw, dh = [i + self.tabpad * 2 for i in (w, h)]
            if not isinstance(view, list):
                view.y += y + dh
                path1 = ui.Path.rounded_rect(x, y, dw, dh, radius)
                path2 = ui.Path.rect(x, y + dh - radius, dw, radius)
                view = [view, path1, path2]
                self.pages[page] = view
            
            view, path1, path2 = view
            
            if view == self.selpage:
                ui.set_color(0.89)
            else:
                ui.set_color(0.82)
            path1.fill()
            path2.fill()
            dy = y + dh/2. - h/2.
            ui.draw_string(page,
                           (x, dy, dw, dh),
                           self.tabfont,
                           self.tabfg,
                           ui.ALIGN_CENTER)
            x += dw
        
    def touch_began(self, touch):
        x, y = touch.location
        for page, [_, path1, _] in self.pages.items():
            if path1.hit_test(x, y):
                self.tappage = [path1, page]
                self.touchid = touch.touch_id
    
    def touch_ended(self, touch):
        x, y = touch.location
        if touch.touch_id == self.touchid:
            if self.tappage[0].hit_test(x, y):
                page = self.tappage[1]
                self.selpage = self.pages[page][0]
                self.setPage(page)
        self.touchid = None
        self.tappage = None
        self.set_needs_display()
