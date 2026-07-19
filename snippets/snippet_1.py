# ejemplo mínimo: bucket policy que impide sobreescritura silenciosa
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "DenyOverwriteOfLockedRoot",
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::ml-prompt-roots/listing/*",
    "Condition": {
      "StringNotEqualsIfExists": {
        "s3:object-lock-mode": "COMPLIANCE"
      },
      "Bool": { "aws:RequestObjectLockEnabled": "true" }
    }
  }]
}