/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* curr = head;
    while (curr != NULL && curr->next != NULL) {
        if (curr->val == curr->next->val) {
            // remove curr->next
            struct ListNode* tmp = curr->next;
            curr->next = tmp->next;
            free(tmp);
        } else {
            curr = curr->next;
        }
    }
    return head;    
}