from django.db import models

class LeaveRequest(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('annual', 'Annual Leave'),
        ('sick', 'Sick Leave'),
        ('unpaid', 'Unpaid Leave'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    leave_start = models.DateTimeField()
    leave_end = models.DateTimeField()
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    reason = models.TextField()
    total_days = models.IntegerField()
    total_left = models.IntegerField()
    def serialize(self):
      return {
        # other fields
          'leave_end': self.leave_end.isoformat(),
          'leave_start': self.leave_start.isoformat()
        }