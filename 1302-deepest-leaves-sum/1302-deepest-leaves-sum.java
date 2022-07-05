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
    public int deepestLeavesSum(TreeNode root) {
        int level = getLevel(root);
        return getLeaveAtLevel(root, level);
    }
    
    public int getLeaveAtLevel(TreeNode root, int level){
        if(root == null) return 0;
        if(level == 1 ) return root.val;
        return getLeaveAtLevel(root.left, level-1) +   getLeaveAtLevel(root.right, level-1);
    }
    
    public int getLevel(TreeNode root){
        if(root == null) return 0;
        return Math.max(getLevel(root.left) + 1, getLevel(root.right) + 1); 
    }
}
