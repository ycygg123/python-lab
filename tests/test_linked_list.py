import pytest

from app.main import Linked_list


def test_new_list_is_empty():
    """新建的链表，长度应该是 0"""
    ll = Linked_list()          # 准备
    assert len(ll) == 0         # 断言


def test_add_node_increases_size():
    """加一个节点，长度变 1"""
    ll = Linked_list()
    ll.add_new_node(1)
    assert len(ll) == 1


def test_add_node_is_push_front():
    """头插：最后加的排最前面"""
    ll = Linked_list()
    ll.add_new_node(1)
    ll.add_new_node(2)
    ll.add_new_node(3)
    assert ll.to_list() == [3, 2, 1]


def test_pop_returns_head_value():
    """pop 要返回被删掉的那个值"""
    ll = Linked_list()
    ll.add_new_node(1)
    ll.add_new_node(2)
    assert ll.pop_top_node() == 2
    assert len(ll) == 1
    assert ll.to_list() == [1]


def test_pop_from_empty_raises():
    """空链表 pop 应该报 IndexError"""
    ll = Linked_list()
    with pytest.raises(IndexError):
        ll.pop_top_node()


def test_pop_until_empty():
    """全部删光后：长度为 0、列表为空、而且不能崩"""
    ll = Linked_list()
    ll.add_new_node(1)
    ll.add_new_node(2)
    ll.pop_top_node()
    ll.pop_top_node()
    assert len(ll) == 0
    assert ll.to_list() == []


def test_order_after_mixed_operations():
    """混合操作后顺序仍然正确"""
    ll = Linked_list()
    for i in range(1, 6):       # 1..5 依次头插 → [5, 4, 3, 2, 1]
        ll.add_new_node(i)
    ll.pop_top_node()           # 删掉 5 → [4, 3, 2, 1]
    ll.add_new_node(9)          # 头插 9 → [9, 4, 3, 2, 1]
    assert ll.to_list() == [9, 4, 3, 2, 1]
    assert len(ll) == 5
