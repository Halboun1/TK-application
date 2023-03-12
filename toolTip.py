import tkinter as tk

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None

    def show_tip(self):
        "Display text in tooltip window"
        if self.tip_window or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x , y - 18))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#FFFFFF", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        "Hide tooltip window"
        if self.tip_window:
            self.tip_window.destroy()
        self.tip_window = None

def create_tooltip(widget, text):
    tooltip = ToolTip(widget, text)
    widget.bind("<Enter>", lambda event: tooltip.show_tip())
    widget.bind("<Leave>", lambda event: tooltip.hide_tip())
