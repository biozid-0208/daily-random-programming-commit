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
    int max = 0;
    int maxDept(TreeNode root){
        if(root == null) return 0;
        int left = maxDept(root.left);
        int right = maxDept(root.right);
        max = Math.max(max, right+ left);
        return  Math.max(right, left) + 1 ;
    }
    public int diameterOfBinaryTree(TreeNode root) {
       maxDept(root) ;   
        return max;
    }
}