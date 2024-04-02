from django.db import models
from users.models import User
from excelupload.models import proformaItem, proformaItemMaster

# Create your models here.


class orderAcknowledgement(models.Model):
    OrderAckId = models.AutoField(primary_key=True, unique=True)
    # ProformaID = models.IntegerField(null=True, blank=True)
    ProformaID = models.ForeignKey(proformaItemMaster, null=True, on_delete=models.CASCADE)
    RevNo = models.IntegerField(null=True)
    Advance = models.FloatField(default=0.00, null=True)
    Retention = models.FloatField(default=0.00, null=True)
    MaterialReadinessDate = models.DateField(null=True, blank=True)
    Freight = models.FloatField(default=0.00, null=True)
    TotalAmount = models.FloatField(default=0.00, null=True)
    SubmittedBy = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    SubmittedDate = models.DateTimeField(auto_now_add=True, null=True)
    DeleteFlag = models.BooleanField(null=True)
    CategoryId = models.IntegerField(null=True)
    DivisionId = models.IntegerField(null=True)
    RegionId = models.IntegerField(null=True)
    ProjectManagerId = models.IntegerField(null=True)
    JobCode = models.CharField(null=True, max_length=50)
    WBS = models.CharField(null=True, max_length=50)
    Party_Address = models.CharField(null=True, max_length=50)
    DeletedBy = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    DeletedOn = models.DateTimeField(null=True)
    TotalUnitPrice = models.FloatField(default=0.00, null=True)
    TCSApplicable = models.CharField(null=True, max_length=50)
    TCS = models.FloatField(default=0.00, null=True)
    TCSAmount = models.FloatField(default=0.00, null=True)
    TotalAmountWithTCS = models.FloatField(default=0.00, null=True)
    GSTBaseValue = models.FloatField(default=0.00, null=True)
    PI_DueDays = models.IntegerField(null=True)
    PI_DueDate = models.DateField(null=True)
    PI_Remarks = models.CharField(null=True, max_length=50)

    PI_TotalDiscount = models.FloatField(default=0.00, null=True)
    PI_TotalPf = models.FloatField(default=0.00, null=True)
    PI_TotalFreight = models.FloatField(default=0.00, null=True)
    PI_TotalSGST = models.FloatField(default=0.00, null=True)
    PI_TotalCGST = models.FloatField(default=0.00, null=True)
    PI_TotalIGST = models.FloatField(default=0.00, null=True)

    #PI_BasicValuePercentage = models.FloatField(default=0.00, null=True) # by gautam 05-02-2024
    #PI_GstPercentage = models.FloatField(default=0.00, null=True)      # by gautam 05-02-2024

    PI_BasicValuePercentage = models.IntegerField(default=0.00, null=True) # by gautam 05-02-2024
    PI_GstPercentage = models.IntegerField(default=0.00, null=True)      # by gautam 05-02-2024

    PI_NO = models.IntegerField(null=True)
    PI_CODE = models.CharField(max_length=100, null=True)

    UpdatedBy = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    UpdatedDate = models.DateTimeField(auto_now_add=True, null=True)
    deleted_remarks = models.CharField(max_length=500, null=True)

    objects = models.Manager()


class orderAcknowledgementHistory(models.Model):
    OrderAck_HistoryId = models.AutoField(primary_key=True, unique=True)
    OrderAckId = models.ForeignKey(orderAcknowledgement, related_name='order', on_delete=models.CASCADE)
    ProformaItemid = models.IntegerField(null=True)
    ProformaID = models.IntegerField(null=True)
    Revno = models.IntegerField(null=True)
    Type = models.CharField(null=True, max_length=50)
    Description = models.CharField(null=True, max_length=1000)
    PercentonAmt = models.CharField(null=True, max_length=1000)
    APBGDetails = models.CharField(null=True, max_length=1000)
    PartName = models.CharField(null=True, max_length=255)
    HSN = models.CharField(null=True, max_length=50)
##    Qty = models.IntegerField(null=True)
    Qty = models.FloatField(default=0.00, null=True, blank=True)
    UOM = models.CharField(null=True, max_length=50)
    UnitPrice = models.FloatField(default=0.00, null=True)
    Advance = models.FloatField(default=0.00, null=True)
    Retention = models.FloatField(default=0.00, null=True)
    MaterialReadinessDate = models.DateField(null=True, blank=True)
    Freight = models.FloatField(default=0.00, null=True)
    IGST = models.FloatField(default=0.00, null=True)
    SGST = models.FloatField(default=0.00, null=True)
    CGST = models.FloatField(default=0.00, null=True)
    PaymentTerms = models.CharField(null=True, max_length=1000)
    SubmittedBy = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    SubmittedDate = models.DateTimeField(auto_now_add=True, null=True)
    UpdatedBy = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    UpdatedDate = models.DateTimeField(auto_now_add=True)
    DeleteFlag = models.BooleanField(null=True)
    DeletedBy = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    category_id = models.IntegerField(null=True)
    division_id = models.IntegerField(null=True)
    region_id = models.IntegerField(null=True)
    TotalAmount = models.FloatField(default=0.00, null=True)
    TotalAdvance = models.FloatField(default=0.00, null=True)
    TotalRetention = models.FloatField(default=0.00, null=True)
    GSTBaseValue = models.FloatField(default=0.00, null=True)

##    PI_Qty = models.IntegerField(null=True)
    PI_Qty = models.FloatField(default=0.00, null=True, blank=True)
    PI_Discount = models.FloatField(default=0.00, null=True)
    PI_Pf = models.FloatField(default=0.00, null=True)
    PI_Freight = models.FloatField(default=0.00, null=True)
    PI_SGST = models.FloatField(default=0.00, null=True)
    PI_CGST = models.FloatField(default=0.00, null=True)
    PI_IGST = models.FloatField(default=0.00, null=True)
    # PI_TotalAmount = models.FloatField(default=0.00, null=True)
    # PI_Sum_of_TotalAmount = models.FloatField(default=0.00, null=True)

    objects = models.Manager()


