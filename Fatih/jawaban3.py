MaxDist = 626

class Graph :
	def __init__(Self, Row, Column) :
		Self.Row = Row
		Self.Column = Column
		Self.Matrix = []
		Self.Vertex = []
		Self.Start = None
		Self.Exit = None
		
	def GetDistance(Self, Start, End) :
		#Kompleksitas : max(baris, kolom)
		Result = 0
		
		if Start[1] > End[1] or Start[0] > End[0] :
			Start, End = End, Start
			
		if Start[0] == End[0] :
			for i in range(Start[1], End[1]) :
				if Self.Matrix[Start[0]][i] == '#' :
					Result +=1
					
		elif Start[1] == End[1] :
			for i in range(Start[0], End[0]) :
				if Self.Matrix[i][Start[1]] == '#' :
					Result +=1
		return Result * Result
		
	def GetAdjacent(Self, Vertex) :
		Adjacent = []
		
		#Kompleksitas : banyaknya vertex
		#for v in Self.Vertex :
			#if v != Vertex :
				#if v[0] == Vertex[0] or v[1] == Vertex[1] :
					#Adjacent.append(v)
		
		#Kompleksitas : baris + kolom
		if Self.Matrix[Vertex[0]][Vertex[1]] != '#' :		
			for i in range(Self.Column) :
				if i != Vertex[1] and Self.Matrix[Vertex[0]][i] != '#' :
					Adjacent.append([Vertex[0], i])
				
			for i in range(Self.Row) :
				if i != Vertex[0] and Self.Matrix[i][Vertex[1]] != '#' :
					Adjacent.append([i, Vertex[1]])
					
		return Adjacent
					
	def Dijkstra(Self) :
		#Kompleksitas : banyaknya vertex * (baris + kolom) + (banyaknya tetangga * max(baris, kolom))
		Dist = []
		Visited = []
		for i in range(Self.Row) :
			Dist.append([MaxDist] * Self.Column)
			Visited.append([False] * Self.Column)
			
		Dist[Self.Start[0]][Self.Start[1]] = 0
		
		while True :
			Vertex = None
			
			#GetNearestVertex
			NearestDist = MaxDist
			for v in Self.Vertex :
				if Dist[v[0]][v[1]] < NearestDist and not Visited[v[0]][v[1]] :
					NearestDist = Dist[v[0]][v[1]]
					Vertex = v
				
			if Vertex is None :
				break

			Visited[Vertex[0]][Vertex[1]] = True
			
			Adjacent = Self.GetAdjacent(Vertex)
			for v in Adjacent :
				Dist[v[0]][v[1]] = min(Dist[v[0]][v[1]], Dist[Vertex[0]][Vertex[1]] + Self.GetDistance(Vertex, v))
				
		return Dist[Self.Exit[0]][Self.Exit[1]]

T = int(input())
for t in range(T) :
	Row, Column = map(int, input().split())
	G = Graph(Row, Column)

	for i in range(Row) :
		Arr = list(input())
		for j in range(Column) :
			if Arr[j] != '#' :
				if Arr[j] == 'S' :
					G.Start = [i, j]
				elif Arr[j] == 'E' :
					G.Exit = [i, j]
				G.Vertex.append([i, j])
		
		G.Matrix.append(Arr)
	
	print("Case #{}: ".format(t + 1), end = '')	
	Result = G.Dijkstra()
	if Result == MaxDist :
		print(-1)
	else :
		print(Result)