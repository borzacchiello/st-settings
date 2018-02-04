import sublime, sublime_plugin

class LineBookmarkCommand(sublime_plugin.TextCommand):

    def run(self, edit, line):
        line = int(line) - 1

        pt = self.view.text_point(line, 0)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(pt))
        self.view.show(pt)

        self.view.run_command("toggle_bookmark")

class HighlightLinesCommand(sublime_plugin.WindowCommand):

    def on_done(self, string):
        lines = []
        fin = open(string, "r")
        for line in fin:
            try:
                line_number = int(line)
                self.window.views()[0].run_command("line_bookmark", {"line": line_number})
            except:
                pass
        fin.close()


    def run(self):
        self.window.show_input_panel("Please enter the directory name:", "", self.on_done, None, None)
