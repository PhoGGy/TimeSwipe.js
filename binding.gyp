{
    "targets": [{
        "target_name": "timeswipe",
        "cflags!": [ "-fno-exceptions", "-Wall" ],
        "cflags_cc!": [ "-fno-exceptions", "-Wall" ],
        "sources": [
            "napi.cpp"
        ],
        'include_dirs': [
            "<!@(node -p \"require('node-addon-api').include\")",
            "<!@(node -p \"require('napi-thread-safe-callback').include\")",
            "$(TARGET_DIR)/usr/include"
        ],
        'libraries': [
            "$(TARGET_DIR)/usr/lib/libtimeswipe.so",
        ],
        'dependencies': [
            "<!(node -p \"require('node-addon-api').gyp\")"
        ],
        'defines': [ ]
    }]
}
