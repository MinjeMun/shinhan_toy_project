from django.db import models

# Create your models here.

class Order(models.Model):
    ord_ymd = models.CharField(max_length=16, verbose_name='ORD_YMD')
    acct_mang_dbrn_code = models.CharField(max_length=16, verbose_name='ACCT_MANG_DBRN_CODE')
    ord_no = models.IntegerField(verbose_name='ORD_NO')
    acct_no = models.CharField(max_length=64, verbose_name='ACTT_NO')
    callv_type_code = models.CharField(max_length=32, verbose_name='CALLV_TYPE_CODE')
    sell_buy_tp_code = models.IntegerField(verbose_name='SELL_BUY_TP_CODE')
    stbd_code = models.CharField(max_length=16, verbose_name='STBD_CODE')
    ord_qty = models.IntegerField(verbose_name='ORD_QTY')
    ord_uv = models.IntegerField(verbose_name='ORD_UV')
    mrgn_base_uv = models.IntegerField(verbose_name='MRGN_BASE_UV')

    class Meta:
        db_table='shinhan_order'
        verbose_name='주문정보'
        verbose_name_plural='주문정보'

class Comment(models.Model):
    # ForeignKey 지정 시 on_delete 꼭 필요 (해당 member가 사라지면 어떻게 처리할지 정책을 정함(CASCADE))
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='작성자') 
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, verbose_name='주문명')
    content = models.TextField(verbose_name='댓글')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_comment'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'

# migrations 파일은 수정 절대 x => model에서 변경하고 다시 migraiton 하면 수정된 것들이 반영됨