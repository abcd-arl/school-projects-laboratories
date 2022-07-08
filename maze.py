import tkinter as tk
from util import initialize_graph
from a_star import astar_search

class Maze:
	def __init__(self, horizontal_lines, vertical_line):
		self.graph = initialize_graph()
		
		self.horizontal_lines = horizontal_lines
		self.vertical_lines = vertical_lines
		self.square_size = 80
		
		self.root = tk.Tk()
		self.c = tk.Canvas(bg="white", width=(len(horizontal_lines)-1)*self.square_size, 
									   height=((len(vertical_lines))*self.square_size))
				   
		self.var = []
		self.path, self.explored_nodes = astar_search(initialize_graph(), '0', '61')
	
	def find_path(self):
		self.c.after(0, self.explored_path, enumerate(self.explored_nodes))
		self.c.after(5000, self.final_path, enumerate(self.path))
		
	def final_path(self, path_iter):
		i, j = next(path_iter)
		x, y = divmod(int(j), 8)
		self.var.append(self.c.create_rectangle((x+1)*80, 
												(y+1)*80, (x+2)*80, (y+2)*80,
												outline="green", 
												fill="#fafa78",
												tag="highlight"))
		self.c.tag_lower("highlight")
		self.c.after(100, self.final_path, path_iter)
		
		
	def explored_path(self, path_iter):
		i, j = next(path_iter)
		x, y = divmod(int(j), 8)
		self.var.append(self.c.create_rectangle((x+1)*80, 
												(y+1)*80, (x+2)*80, (y+2)*80,
												outline="green", 
												fill="#ffffcc",
												tag="highlight"))
		self.c.tag_lower("highlight")
		self.c.after(100, self.explored_path, path_iter)
		
	def clear_path(self):
		for i in self.var:
			self.c.delete(i)
		
	def draw_maze(self):
		self.c.pack()
		self.c.create_rectangle((0+1)*80, (0+1)*80, (0+2)*80, (0+2)*80, outline="yellow", fill="lime")
		self.c.create_rectangle((7+1)*80, (5+1)*80, (7+2)*80, (5+2)*80, outline="yellow", fill="indian red")
		
		var = list()
		
		for row_num, row in enumerate(horizontal_lines):
			for col_num, line in enumerate(row):
				line_size, line_color = line
				x_start, y_start = col_num * self.square_size, row_num * self.square_size
				if line_size:
					self.c.create_line(x_start - 2,
									   y_start,
									   x_start + self.square_size + 2,
									   y_start,
									   width=line_size,
									   fill=line_color)

		for row_num, row in enumerate(vertical_lines):
			for col_num, line in enumerate(row):
				line_size, line_color = line
				x_start, y_start = col_num*self.square_size, row_num*self.square_size
				if line_size:
					self.c.create_line(x_start,
								   	   y_start,
									   x_start,
									   y_start + self.square_size,
									   width=line_size,
									   fill=line_color)

		for i in range(8):
			self.c.create_text((i+1)*80+40, 40, text=str(i))
			self.c.create_text(40, (i+1)*80+40, text=str(i))
			for j in range(8):
				self.c.create_text((i+2)*80-40, (j+2)*80-40, text=str(i*8+j))
				
		button_frame = tk.Frame(self.root, height=100)
		button_frame.pack(fill=tk.X)
		
		button1 = tk.Button(button_frame, text='Find A Star path', height=4, width=35, bg='light yellow', command=self.find_path)
		button1.pack(side=tk.LEFT)
		
		button2 = tk.Button(button_frame, text='Clear', height=4, width=26, bg='#ffccb3', command=self.clear_path)
		button2.pack(side=tk.LEFT)
				
		self.root.mainloop()
				
if __name__ == "__main__":
	
	t = (2, 'light grey')
	T = (4, 'black')
	n = (0, 'none')
		
	horizontal_lines = [
		[t, t, t, t, t, t, t, t, t],
		[t, T, T, T, T, T, T, T, T],
		[t, n, n, n, n, n, T, T, n],
		[t, n, T, T, n, n, n, n, n],
		[t, T, T, n, n, n, n, T, n],
		[t, n, T, n, T, n, n, T, n],
		[t, n, n, T, n, n, n, n, T],
		[t, n, n, n, n, T, n, T, T],
		[t, T, n, T, n, n, T, T, n],
		[t, T, T, T, T, T, T, T, T]]

	vertical_lines = [
		[t, t, t, t, t, t, t, t, t, t],
		[t, t, n, n, n, T, n, n, n, T],
		[t, T, T, T, T, T, T, n, T, T],
		[t, T, n, n, T, T, T, n, T, T],
		[t, T, n, n, T, n, T, n, n, T],
		[t, T, T, T, n, T, T, T, T, T],
		[t, T, T, n, T, T, T, n, n, n],
		[t, T, T, T, T, T, n, T, n, T],
		[t, T, n, n, n, T, n, n, n, T]]
		
	m = Maze(horizontal_lines, vertical_lines)
	m.draw_maze()
