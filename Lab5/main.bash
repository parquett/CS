#!/bin/bash

# Step 1: Create Root CA (self-signed certificate)
echo "Generating Root CA..."
openssl genrsa -out rootCA.key 4096
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 3650 -out rootCA.crt -subj "/CN=MyRootCA"

# Step 2: Generate User Private Key and CSR
echo "Generating User Key and CSR..."
openssl genrsa -out user.key 2048
openssl req -new -key user.key -out user.csr -subj "/CN=User"

# Step 3: Sign User Certificate with Root CA
echo "Signing User Certificate..."
openssl x509 -req -in user.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out user.crt -days 365 -sha256

# # Step 4: Revocation Setup
 echo "Creating Certificate Revocation List (CRL)..."
 openssl ca -keyfile rootCA.key -cert rootCA.crt -gencrl -out rootCA.crl

# Step 5: Demonstrate Signing a File
DOCUMENT="document.txt"
SIGNATURE="document.sig"
VERIFICATION_OUTPUT="verification_output.txt"

# Create a sample file to sign
echo "This is a sample document for signing." > $DOCUMENT

# Sign the file
echo "Signing the document with User's private key..."
openssl dgst -sha256 -sign user.key -out $SIGNATURE $DOCUMENT

# Verify the signature
echo "Verifying the signature with User's public key..."
openssl dgst -sha256 -verify <(openssl x509 -in user.crt -pubkey -noout) -signature $SIGNATURE $DOCUMENT > $VERIFICATION_OUTPUT 2>&1

# Display the result of verification
if grep -q "Verified OK" "$VERIFICATION_OUTPUT"; then
    echo "Signature Verified Successfully!"
else
    echo "Signature Verification Failed!"
fi

# # Step 6: Demonstrate Certificate Revocation
 echo "Revoking User Certificate..."
 openssl ca -keyfile rootCA.key -cert rootCA.crt -revoke user.crt

 echo "Updating CRL after revocation..."
 openssl ca -keyfile rootCA.key -cert rootCA.crt -gencrl -out rootCA.crl

 # Display CRL content for reference
 echo "Certificate Revocation List (CRL):"
 cat rootCA.crl

echo "PKI setup and demonstration complete!"
