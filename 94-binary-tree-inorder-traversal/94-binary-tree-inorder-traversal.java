/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> s = new Stack<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
        TreeNode cur = root;
        while(cur != null || !s.empty()){
        
            if(cur != null) {
                s.push(cur);
                cur = cur.left;
            }
            else{
                cur = s.pop();
                res.add(cur.val);
                cur = cur.right;
            }
        }
        return res;
    }
}