#include <Adafruit_ADS1X15.h>
#include <TroykaI2CHub.h>
const int NUM_CHANNELS = 8;
uint8_t adr_hub[NUM_CHANNELS] = {0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77};
uint8_t adr_ads[4] = {0x48, 0x49, 0x4A, 0x4B};

int memoryFree(){
  extern int *__brkval;
  int freeValue; 
    if((int)__brkval == 0) {
      freeValue = ((int)&freeValue) - ((int)__malloc_heap_start);
    }else {
      freeValue = ((int)&freeValue) - ((int)__brkval);
    }
  return freeValue;
}

class MUX {
  public :

    uint8_t adr_hub;
    bool status[NUM_CHANNELS];
    int16_t results[NUM_CHANNELS];
    String value[NUM_CHANNELS];
    Adafruit_ADS1X15 ads[NUM_CHANNELS];
    TroykaI2CHub hub;

    MUX(uint8_t adr_hub) : adr_hub(adr_hub)
    {
      //hub объявлен в private
      this->hub = TroykaI2CHub::TroykaI2CHub(adr_hub);
    }

  bool *begin()
  {

    hub.begin();

    for(int i = 0; i < NUM_CHANNELS; i++)
    {
      this->hub.setBusChannel(i);
      status[i] = !this->ads[i].begin(adr_ads[0]); 
    }
    return status;
  }

  String *read()
  {
    for(int i = 0; i < NUM_CHANNELS; i++)
    {
      if(status[i] == 1)
      {
        value[i] = "nc";
      }
      else
      {
        this->hub.setBusChannel(i);
        results[i] = this->ads[i].readADC_Differential_0_1();
        value[i] = String((results[i] * multiplier)/1000);
      }
    }
    return value;
  }

  private:
    float multiplier = 0.1875F;

};

MUX mux(0x71);

void setup() {
  Serial.begin(9600);
  mux.begin();
}

void loop() {
  String *value = mux.read();
  Serial.print(mux.adr_hub); Serial.print(";"); 
  for(int i = 0; i < NUM_CHANNELS; i++)
  {
    if(i==7)
    {
      Serial.print(i); Serial.print(":"); Serial.println(value[i]); 

    }
    else
    {
      Serial.print(i); Serial.print(":"); Serial.print(value[i]); Serial.print(";");
    }
    
  }

  //Serial.println(memoryFree());
}
