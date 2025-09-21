class TrieNode {
      TrieNode[] children;
      boolean isLeaf;
      {
          children= new TrieNode[26];
          isLeaf=false;
      }
}
class Trie{
        TrieNode root;
        public Trie() {root=new TrieNode();}
    public void insert(String key) {
        TrieNode curr=root;
        for(char c : key.toCharArray()){
            if(curr.children[c - 'a'] == null){
                curr.children[c - 'a']= new TrieNode();
            }
            curr=curr.children[c - 'a'];
        }
        curr.isLeaf=true;
    }
    public boolean search(String key) {
        TrieNode curr=root;
        for(char c : key.toCharArray()){
            if(curr.children[c - 'a'] == null){
                return false;
            }
            curr=curr.children[c - 'a'];
        }
        return curr.isLeaf;
    }
    public boolean isPrefix(String prefix) {
        TrieNode curr=root;
        for(char c : prefix.toCharArray()){
            if(curr.children[c - 'a'] == null){
                return false;
            }
            curr=curr.children[c - 'a'];
        }
        return true;
    }
    public static void main(String[] args){
        Trie trie=new Trie();
        String[] arr={"and","do","dad"};
        for(String s : arr){
            trie.insert(s);
        }
        String[] searchKeys={"do","gee","bat"};
        for(String s : searchKeys){
            if(trie.search(s))
            System.out.println("true");
            else
            System.out.println("false");
        }
        System.out.println();
        String[] prefixKeys={"ge","ba","do","de"};
        for(String s : prefixKeys){
            if(trie.isPrefix(s))
            System.out.println("true");
            else
            System.out.println("false");
        }
        }
    }
