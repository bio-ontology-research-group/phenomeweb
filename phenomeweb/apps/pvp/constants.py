QUERY_STATUS = (PENDING, PROCESSING, FINISHED) = (
    'Pending', 'Processing', 'Finished')

INHERITANCE_MODES = ('dominant', 'recessive', 'x-linked', 'others', 'unknown')
INHERITANCE_MODE_CHOICES = zip(INHERITANCE_MODES, INHERITANCE_MODES)
