import java.util.*;

public class BellmanFord {
    static int[] bellmanFord(int V, int[][] edges, int src) {
        int[] dist = new int[V];
        Arrays.fill(dist, (int)1e8);
        dist[src] = 0;

        for (int i = 0; i < V - 1; i++) {
            for (int[] edge : edges) {
                int u = edge[0], v = edge[1], wt = edge[2];
                if (dist[u] != (int)1e8 && dist[u] + wt < dist[v]) {
                    dist[v] = dist[u] + wt;
                }
            }
        }

        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], wt = edge[2];
            if (dist[u] != (int)1e8 && dist[u] + wt < dist[v]) {
                return new int[]{-1};
            }
        }

        return dist;
    }

    public static void main(String[] args) {
        int V = 5;
        int[][] edges = {
            {0, 1, 5},
            {1, 2, -2},
            {1, 5 - 2, 1},
            {2, 3, 3},
            {3, 4, 2}
        };

        System.out.println(Arrays.toString(bellmanFord(V, edges, 0)));
    }
}
