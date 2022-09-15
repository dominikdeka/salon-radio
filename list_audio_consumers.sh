#!/bin/sh
for i in /proc/asound/card?/pcm*/sub?/hw_params;
 do echo $i; cat $i;
done