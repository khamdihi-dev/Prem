import zlib, base64, marshal
exec(marshal.loads(zlib.decompress(base64.b64decode('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'))))