/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Create a dummy node to act as the start of the merged list
    struct ListNode dummy;
    struct ListNode* cur = &dummy;
    dummy.next = NULL;

    // Traverse both lists and merge them
    while (list1 != NULL && list2 != NULL) {
        if (list1->val < list2->val) {
            cur->next = list1;
            list1 = list1->next;
        } else {
            cur->next = list2;
            list2 = list2->next;
        }
        cur = cur->next;
    }

    // If one of the lists is not exhausted, link the rest of it
    if (list1 != NULL) {
        cur->next = list1;
    } else {
        cur->next = list2;
    }

    // Return the merged list, which starts after the dummy node
    return dummy.next;
}
