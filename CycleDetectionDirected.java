import java.util.*;

public class CycleDetectionDirected {
    static boolean dfs(int node, ArrayList<ArrayList<Integer>> adj, boolean[] visited, boolean[] pathVisited) {
        visited[node] = true;
        pathVisited[node] = true;

        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, adj, visited, pathVisited)) return true;
            } else if (pathVisited[neighbor]) {
                return true;
            }
        }

        pathVisited[node] = false;
        return false;
    }

    static boolean isCyclic(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[V];
        boolean[] pathVisited = new boolean[V];

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (dfs(i, adj, visited, pathVisited)) return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int V = 4;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());

        adj.get(0).add(1);
        adj.get(1).add(2);
        adj.get(2).add(3);
        adj.get(3).add(1);

        System.out.println(isCyclic(V, adj));
    }
}
