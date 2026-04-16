import java.util.*;

class Pair {
    int v, wt;
    Pair(int v, int wt) {
        this.v = v;
        this.wt = wt;
    }
}

public class ShortestPathDAG {
    static void topo(int node, ArrayList<ArrayList<Pair>> adj, boolean[] visited, Stack<Integer> st) {
        visited[node] = true;

        for (Pair p : adj.get(node)) {
            if (!visited[p.v]) topo(p.v, adj, visited, st);
        }

        st.push(node);
    }

    static int[] shortestPath(int V, int src, ArrayList<ArrayList<Pair>> adj) {
        boolean[] visited = new boolean[V];
        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < V; i++) {
            if (!visited[i]) topo(i, adj, visited, st);
        }

        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        while (!st.isEmpty()) {
            int node = st.pop();

            if (dist[node] != Integer.MAX_VALUE) {
                for (Pair p : adj.get(node)) {
                    if (dist[node] + p.wt < dist[p.v]) {
                        dist[p.v] = dist[node] + p.wt;
                    }
                }
            }
        }

        return dist;
    }

    public static void main(String[] args) {
        int V = 6;
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());

        adj.get(0).add(new Pair(1, 2));
        adj.get(0).add(new Pair(4, 1));
        adj.get(1).add(new Pair(2, 3));
        adj.get(4).add(new Pair(2, 2));
        adj.get(2).add(new Pair(3, 6));
        adj.get(4).add(new Pair(5, 4));
        adj.get(5).add(new Pair(3, 1));

        System.out.println(Arrays.toString(shortestPath(V, 0, adj)));
    }
}
