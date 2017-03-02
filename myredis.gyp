{
   'targets': [  
     {  
       'target_name': 'myredis',
       'type': 'executable',
       'include_dirs': [
          'include',
          'include/hiredis',
          'include/uv',
        ],
       'sources': [
         './src/main.cpp',
         
        ],
       'conditions': [
          [ 'OS=="mac"', {
              'libraries':[
                './libs/macos/libuv.a',
                './libs/macos/libhiredis.a',
              ],
              'xcode_settings': { 'ARCHS': ['x86_64'], 'SDKROOT':'macosx', 'MACOSX_DEPLOYMENT_TARGET':'10.11','OTHER_LDFLAGS':'-pagezero_size 10000 -image_base 100000000'},
              
            },
         ],
         [ 'OS=="linux"', {
              'libraries':[
                './libs/ubuntu/libuv.a',
              ],
              'link_settings': {
                'libraries': [ '-ldl', '-lrt' ],
              },
              'cflags':['-g','-fstack-protector','-fstack-protector-all'],
            },
         ],
         
       ],
       'defines': [ 'SERVER_DEBUG', 'ENABLE_CJSON_GLOBAL' ],
     },
   ],  
 }  
