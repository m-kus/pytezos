from unittest import TestCase
from unittest import skip

from pytezos.contract.interface import ContractInterface

source = """
storage (bytes);
parameter (pair (chest_key) (chest));
code {
       UNPAIR;
       DIP {DROP};
       UNPAIR;
       DIIP {PUSH nat 1000};
       OPEN_CHEST;
       IF_LEFT
         { # successful case
           NIL operation;
           PAIR ;
         }
         {
           IF
             { # first type of failure
               PUSH bytes 0x01;
               NIL operation;
               PAIR;
             }
             { # second type of failure
               PUSH bytes 0x00;
               NIL operation;
               PAIR;
             }
         }
     }
"""

chest_key = bytes.fromhex(
    'ac91a7a0efcd9e97bdc29f8c8184e3c5d8dbea9eb284e1a3fdd9bafa9c8380d5f793cbb4ac869cfbafac82c7f896a991a48ef48bb79189a2a997a3bee183b4f8dce0d4e781869ac0d5ab8ad3a48894bfb690b4d6b3b1a7fdcbf6f39a87bac7b59cf9a3b9d1d2d09ea1ca8af9fee7acac82e89aeea09ee7a1acf38dddc2d8bdb9e6ffced5da9cb4d284d9f692d29bc28cadc6ead09bd9b2ffe8ccb392ef8c96e9b7a3d3c0b9caceb3dee6b9dcefb5ff98a9e98186edb69bbbdec8f48490c897ecd5d0dbc587dedac3fba6e2beb4d6f5e2e3c9e4dfdbfcc0b182dff283efbfdbdba997c0c6bdcedc85d5e19a89bf9c8484dfe3c0d1deb08ceffb96bad9edffbfe4f6dfb882b1eddcbdbef39297b0b4d19bfb988185859ba795f9dfffc6b5f4b6e8d6fbe28303c1fadc829d9bf1a992cae0c3c2acd7a2bb8bbe93cb87b7e1aec883aada82c7fac889f1dfe6e2bab8f18f9087aebffef0b3ab8bfed9a5be84a9a7bcabf2dfb0c4d399b7b3dda9deadecf0c1e491cac4a49e8ca5aadebef39dc4dae8b1d3bb93c8ebb0f6c586c0d7cba1cbfccaabf0cbdd95969fa4b3f59af3fa8ca0f1a0f6d09b958eaad8fcd595d1defee1c989b5cadcb9f8a7bfaea1e2969899ee83ffd8e683f9dec4decfe0aff1d5c2dcd3abb6c8c6bce4c8e2f79eb6fde3b8a3a3add5fad4e5ebc8de93ae909ffb8cccc3e6a9ed8ed6b8cd88cab29086d4e8f99be4bebf84f494b0f5fce4e0c4d092e4ce80cca0a7c69fb2bef380ece0e189d9ede0eac9f5a4a5d2f79a9094dbdf91add38b92e5cbeea680effcea83eee7b697c593ab97adb1eff48402'
)
chest = bytes.fromhex(
    'bea8a8b993f2fdb2c3d7f8a9b4e2bba3def2edd5928a82878a81ace6b8e2c0efc5c7dbe9e6b88bca86b0df94f6b5c4d2d4f7f6e9a183fde1edd2b3fc9d9f9c8de6b7c1e580bdb284d7eca9e485cb84b8e386bfa09fe297c5df94eacdd9c090e6eab39aa6ffa69df9fabec2d6b5ba94a6bec4c387dae38ec6b7bdf793e1edb8d2c5e49bd7c1ba84b69afe89d3bd9799bfadfec2e2ddcc88b8d2e0a99f9cc9b0deb682b1c6c8d1bea2e695b2ebd1a6d8eebeddeea3a4b2d983d6cc9cd1a8d0e0c4f4cb8fffb9ddd1f9abb4dbc3ee808cf1cbbd91c7e4859eecfad5b2add3d4b8dae7e0fdabc9f0b29ac78784b7bd8bcaed91ca93cb95ccd79ac8d8b184d1f4f8b0fed1d5d3f3b1ed9dfcd5f483b5a581d79ef5cbbe98889b80bd80f0f9fdd5f3bed5f38653a7f490dddec8d782d2b2b8c1bc9999859fbbc2dd97ed9df4b5b9879588c8ea93c4bfbcaed1efeac4e8bdcab1c3818fa8e8e8b3c6978cabf08c8daddaa2fbbf81d88fda95cecb8591fd90d98ad3b29698c5a4e3ac8e95f7dba0ff91a6ff97d1e1f8c9fb9ef6afae95ac908bb4b9b3b8f8ed8780bfbac6f39cf1f7cab980abcacedeac90afe5bfcda8dab990ffb3a2ad9b889e94e8b6d1f099f5cef7dbacd799e0f2ccf9e7b7c6e591bddeee8895cc89f2d9839ef0afe08ed783c7869685f5fca5cdebf9889ef2839a8ebd88eeb8ebfbd5dab8a4ec86a6a488b1b6f8fe828b8fefaaf9dbd6ddddaaeea4d8e6d5fca2dfdd9af1bdeca1bcf09ab898a49dcbc9f3f99f83fdb690c7cbb7cff5cbca88eafe8ff5eec980aadbe4c2be87b7b098adc3bfd6b1b3a106e1cae5665a7f70a26b8e06979288e26222009d7b6e40acb900000021a1fb7e9f43f45b19d4a5ed10cf729c233612d82ea642e09efd90873e66952e97bb'
)


@skip('not implemented')
class OpenChestTestCase(TestCase):
    def test_open_chest(self):
        ci = ContractInterface.from_michelson(source)
        ci.call(chest_key, chest).interpret()
